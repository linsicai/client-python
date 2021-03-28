import json
import uuid


class OpenCTIStix2Splitter:
    def __init__(self):
        # 缓存
        self.cache_index = {}
        # 
        self.elements = []

    def enlist_element(self, item_id, raw_data):
        nb_deps = 1

        # 校验是否在原始数据里面
        if item_id not in raw_data:
            return 0

        # 查缓存命中
        existing_item = self.cache_index.get(item_id)
        if existing_item is not None:
            return existing_item["nb_deps"]

        # Recursive enlist for every refs
        # 取数据
        item = raw_data[item_id]
        for key, value in item.items():
            if key.endswith("_refs"):
                # 数组引用，去取数组数据
                for element_ref in item[key]:
                    nb_deps += self.enlist_element(element_ref, raw_data)
            elif key.endswith("_ref"):
                # 对象引用
                # Need to handle the special case of recursive ref for created by ref
                is_created_by_ref = key == "created_by_ref"
                if is_created_by_ref:
                    # 特殊情况处理    
                    is_marking = item["id"].startswith("marking-definition--")
                    if is_marking is False:
                        nb_deps += self.enlist_element(value, raw_data)
                else:
                    # 取值
                    nb_deps += self.enlist_element(value, raw_data)
        # Get the final dep counting and add in cache
        # 写缓存
        item["nb_deps"] = nb_deps
        self.elements.append(item)
        self.cache_index[item_id] = item  # Put in cache

        # 返回数据
        return nb_deps

    # 拆分批量数据
    def split_bundle(self, bundle, use_json=True) -> list:
        """splits a valid stix2 bundle into a list of bundles
        :param bundle: valid stix2 bundle
        :type bundle:
        :param use_json: is JSON?
        :type use_json:
        :raises Exception: if data is not valid JSON
        :return: returns a list of bundles
        :rtype: list
        """
        # 解析一下入参
        if use_json:
            try:
                bundle_data = json.loads(bundle)
            except:
                raise Exception("File data is not a valid JSON")
        else:
            bundle_data = bundle
            if "objects" not in bundle_data:
                raise Exception("File data is not a valid bundle")

        # 数组转map，入缓存
        raw_data = {}
        # Build flat list of elements
        for item in bundle_data["objects"]:
            raw_data[item["id"]] = item
        for item in bundle_data["objects"]:
            self.enlist_element(item["id"], raw_data)

        # Build the bundles
        bundles = []

        # 做下缓存排序
        def by_dep_size(elem):
            return elem["nb_deps"]
        self.elements.sort(key=by_dep_size)

        # 返回规范化批量数据
        for entity in self.elements:
            bundles.append(self.stix2_create_bundle([entity], use_json))

        return bundles

    @staticmethod
    def stix2_create_bundle(items, use_json):
        """create a stix2 bundle with items

        :param items: valid stix2 items
        :type items:
        :param use_json: use JSON?
        :type use_json:
        :return: JSON of the stix2 bundle
        :rtype:
        """

        bundle = {
            "type": "bundle",
            "id": "bundle--" + str(uuid.uuid4()),
            "spec_version": "2.1",
            "objects": items,
        }
        return json.dumps(bundle) if use_json else bundle

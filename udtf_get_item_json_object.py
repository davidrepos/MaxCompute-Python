# --encoding=utf8--
from odps.udf import BaseUDTF
from odps.udf import annotate
import json

@annotate('string,string->string,string,string,string')
class GetItemJsonObject(BaseUDTF):
    def process(self,itemid:str,jsonProps:str):
        group_props = json.loads(jsonProps)
        for props in group_props['groupProps'][0]['基本信息'.encode('utf-8')]:
            prop_keys = props.keys()
            for key in prop_keys:
                self.forward(itemid,'基本信息'.encode('utf-8'),key,props[key])

# --encoding=utf8--
#coding=utf-8
import json
if __name__ == "__main__":
    
    js = '{"groupProps":[{"基本信息":[{"保修期":"12个月 "},{"净重":"42kg "},{"制冷方式":"直冷 "},{"包装尺寸":"1185x615x975mm "},{"品牌":"Haier/海尔 "},{"型号":"FCD-215SEA "},{"堆码层数极限":"4层 "},{"尺寸":"1150x560x920mm "},{"开门方式":"蝴蝶门 "},{"毛重":"48kg "},{"采购地":"中国大陆 "},{"颜色分类":"白色 "},{"放置方式":"卧式 "},{"功能":"冷藏冷冻 "},{"容量":"201L(含)-250L(含) "},{"冷冻能力":"13kg/24h "},{"耗电量":"0.69Kwh/24h及以下 "},{"能效等级":"二级 "}]}]}'
    js_decode = js.encode('utf8')
    iteminfo = json.loads(js_decode)
    for prop_group_name in iteminfo:
        props_group = iteminfo[prop_group_name]
        for group in props_group:
            for group_key in group:
                print(group_key)
                props = group[group_key]
                for prop_key_value in props:
                    for prop_key in prop_key_value:
                        print('key:%s' % prop_key)
                        print('value: %s' % prop_key_value[prop_key])
                        #print(prop_value)
        
        

                
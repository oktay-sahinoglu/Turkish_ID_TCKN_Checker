import re

class TCKN_Checker:
    @classmethod
    def validate_tckn(cls, tckn):
        if not (isinstance(tckn, int) or (isinstance(tckn, str) and tckn.isdecimal())):
            return False
        tckn_str = str(tckn)
        tckn = list(map(int,tckn_str))
            
        if len(tckn) != 11 or int(tckn[0]) == 0 : 
            return False
            
        if ((sum(tckn[0:9:2])*7) -  sum(tckn[1:8:2]) ) % 10 != tckn[9] :
            return False
        
        if sum(tckn[:10]) % 10 != tckn[10]:
            return False
        
        return True

    @classmethod
    def find_tckn(cls, text):
        tckn_list = []
        for regex_result in re.findall(r"\d{11}", text):
            if cls.validate_tckn(regex_result):
                tckn_list.append(regex_result)
        return tckn_list

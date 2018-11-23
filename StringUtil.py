# -*- coding: utf-8 -*-

import hashlib
import json


class StringUtil:
        
    def applySha(input):
        try:
            sha_signature = hashlib.sha256(input.encode()).hexdigest()
            return sha_signature
        except Exception as error:
            raise error

    def getJson(object):
        json_string = json.dump(object)
        return json_string

    def getDifficultyString(difficulty):
        dif_string = "0" * difficulty
        return dif_string

"""TESTE
result = StringUtil.applySha("confidencial")
print(result)"""
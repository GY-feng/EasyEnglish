import json
import base64
import types
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tmt.v20180321 import tmt_client, models
class Translate:
    def __init__(self,path,id,key):
        '''
        :param path: 切割好的，要转化成string的图片
        :param key: git不可以上传包含敏感信息，所以要先找枫拿个腾讯云ID和KEY，在构造函数这里上传
        :param if: git不可以上传包含敏感信息，所以要先找枫拿个腾讯云ID和KEY，在构造函数这里上传
        '''
        self.path=path
        self.key=key
        self.id=id

        pass
    def image_to_base64(self):
        with open(self.path, "rb") as image_file:
            enstring = base64.b64encode(image_file.read())
            return enstring.decode('utf-8')
        pass
    def Translate_string(self):
        '''
        :return: 返回一个元组，元组的第一个元素是识别出来的英文字符，元组的第二个元素是转化后的的中文。
        '''
        try:
            id = self.id
            key = self.key
            cred = credential.Credential(id, key)
            # 实例化一个http选项，可选的，没有特殊需求可以跳过
            httpProfile = HttpProfile()
            httpProfile.endpoint = "tmt.tencentcloudapi.com"

            # 实例化一个client选项，可选的，没有特殊需求可以跳过
            clientProfile = ClientProfile()
            clientProfile.httpProfile = httpProfile
            # 实例化要请求产品的client对象,clientProfile是可选的
            client = tmt_client.TmtClient(cred, "ap-guangzhou", clientProfile)
            data = self.image_to_base64()
            # 实例化一个请求对象,每个接口都会对应一个request对象
            req = models.ImageTranslateRequest()
            params = {
                "SessionUuid": "session-00001",
                "Scene": "doc",
                "Data": data,
                "Source": "auto",
                "Target": "zh",
                "ProjectId": 0
            }
            req.from_json_string(json.dumps(params))

            # 返回的resp是一个ImageTranslateResponse的实例，与请求对象对应
            resp = client.ImageTranslate(req)
            json_data = resp.to_json_string()
            data = json.loads(json_data)

            source_texts = [i["SourceText"] for i in data["ImageRecord"]["Value"]]
            target_texts = [i["TargetText"] for i in data["ImageRecord"]["Value"]]

            return (" ".join(source_texts), " ".join(target_texts))

        except TencentCloudSDKException as err:
            print(err)

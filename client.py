# -*- coding: utf-8 -*-
from alibabacloud_imageseg20191230.client import Client as imageseg20191230Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util import models as util_models
import os
from config import ACCESS_KEY_ID, ACCESS_KEY_SECRET, REGION_ID, ENDPOINT

def create_client():
    # 初始化配置
    config = open_api_models.Config(
        # 从环境变量中获取 AccessKey
        access_key_id=ACCESS_KEY_ID,
        access_key_secret=ACCESS_KEY_SECRET,
        
        # --- 关键：必须指定正确的 Endpoint ---
        endpoint=ENDPOINT,
        
        # region_id 也建议指定
        region_id=REGION_ID
    )
    return imageseg20191230Client(config)
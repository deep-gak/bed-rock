编程应用 - 生成网页爬虫
=====================

## 知识点

* 生成小马技术网站的网页爬虫

## 官网

https://komavideo.com

## 实战演习/说明讲解

>画面演示

+ 制作网页爬虫提示词脚本
+ 生成代码
+ 运行调试

## 操作步骤

### 制作网页爬虫提示词脚本

#### 准备爬取的网页

https://komavideo.com/playlist/economy/index.html

#### 准备提示词

请帮我写个Python语言的网页爬虫程序，爬取这个utf-8编码的网页：

```
https://komavideo.com/playlist/economy/index.html
```

我要从下面这个html代码块中爬取内容，请帮我抽出标题信息。

```html
            <div class="bg-gray-200">
                <div class="bg-gray-50 p-3 border-b border-gray-300 shadow-xs mb-3">
                    <div class="flex justify-between"><a href="/" class="nuxt-link-active">
                            <div class="flex items-center"><img src="/favicon.ico" alt="小马视频" class="rounded w-5 h-5">
                                <h3 class="pl-1 text-gray-700">
                                    小马视频
                                </h3>
                            </div>
                        </a>
                        <div class="flex items-center"><a href="/tag/"><img src="/images/tag.png" alt="视频标签"
                                    class="w-5 h-5"></a> <a
                                href="https://www.youtube.com/channel/UCazV3A3_1-Mtd6E_auw_ifg" target="_blank"><img
                                    src="/images/youtube.png" alt="小马技术" class="w-5 h-5 ml-3"></a> <a
                                href="https://github.com/komavideo" target="_blank"><img src="/images/github.png"
                                    alt="Github" class="w-5 h-5 ml-3"></a> <a href="https://discord.gg/VSKw72P"
                                target="_blank"><img src="/images/discord.png" alt="Discord"
                                    class="w-5 h-5 ml-3 opacity-80"></a> <a href="http://tools.komavideo.com"
                                target="_blank"><img src="/images/tools.png" alt="小马工具包"
                                    class="w-5 h-5 ml-3 opacity-60"></a> <a href="/about/"><img src="/images/about.png"
                                    alt="关于" class="w-5 h-5 ml-3"></a></div>
                    </div>
                </div>
                <div class="px-4 py-4 md:px-10 md:py-6">
                    <div data-v-41642b9a>
                        <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-2 sm:gap-2 lg:gap-4 xl:gap-5 2xl:gap-6"
                            data-v-41642b9a>
                            <div class="card flex flex-col" data-v-41642b9a>
                                <div class="flex-grow">
                                    <div><img src="https://i.ytimg.com/vi/ii3OfBsw__A/mqdefault.jpg"
                                            alt="【小马学经济2019】课程介绍 p.1" class="card_image"></div>
                                    <div class="px-3 py-2"><a>
                                            <div class="font-bold text-base text-gray-700">【小马学经济2019】课程介绍 p.1</div>
                                        </a></div>
                                </div>
                                <div class="px-3 py-2 border-t border-gray-200">
                                    <div class="flex justify-between">
                                        <div><a href="https://www.youtube.com/playlist?list=PLliocbKHJNwt_NgsZ80l_8z5f6ua-uShq"
                                                target="_blank"><img src="/images/youtube.png" alt="小马技术"
                                                    class="w-5 h-5 opacity-80"></a> <!----></div>
                                        <div class="flex items-center text-xs text-green-700">
                                            10-24 16:19
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="card flex flex-col" data-v-41642b9a>
                                <div class="flex-grow">
                                    <div><img src="https://i.ytimg.com/vi/EvbOXEszAQ4/mqdefault.jpg"
                                            alt="【小马学经济2019】实力真不是盖的 - 各国基础数据(面积，人口，GDP) p.2" class="card_image"></div>
                                    <div class="px-3 py-2"><a>
                                            <div class="font-bold text-base text-gray-700">【小马学经济2019】实力真不是盖的 -
                                                各国基础数据(面积，人口，GDP) p.2</div>
                                        </a></div>
                                </div>
                                <div class="px-3 py-2 border-t border-gray-200">
                                    <div class="flex justify-between">
                                        <div><a href="https://www.youtube.com/playlist?list=PLliocbKHJNwt_NgsZ80l_8z5f6ua-uShq"
                                                target="_blank"><img src="/images/youtube.png" alt="小马技术"
                                                    class="w-5 h-5 opacity-80"></a> <!----></div>
                                        <div class="flex items-center text-xs text-green-700">
                                            11-01 10:44
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="card flex flex-col" data-v-41642b9a>
                                <div class="flex-grow">
                                    <div><img src="https://i.ytimg.com/vi/favJ_K1vlpo/mqdefault.jpg"
                                            alt="【小马学经济2019】你信教吗 - 各国宗教比例 p.3" class="card_image"></div>
                                    <div class="px-3 py-2"><a>
                                            <div class="font-bold text-base text-gray-700">【小马学经济2019】你信教吗 - 各国宗教比例 p.3
                                            </div>
                                        </a></div>
                                </div>
                                <div class="px-3 py-2 border-t border-gray-200">
                                    <div class="flex justify-between">
                                        <div><a href="https://www.youtube.com/playlist?list=PLliocbKHJNwt_NgsZ80l_8z5f6ua-uShq"
                                                target="_blank"><img src="/images/youtube.png" alt="小马技术"
                                                    class="w-5 h-5 opacity-80"></a> <!----></div>
                                        <div class="flex items-center text-xs text-green-700">
                                            11-09 10:26
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="card flex flex-col" data-v-41642b9a>
                                <div class="flex-grow">
                                    <div><img src="https://i.ytimg.com/vi/yCSrl8iU6UQ/mqdefault.jpg"
                                            alt="04【小马学经济2019】交钱多的说上句 - 联合国的份子钱 p.4" class="card_image"></div>
                                    <div class="px-3 py-2"><a>
                                            <div class="font-bold text-base text-gray-700">04【小马学经济2019】交钱多的说上句 -
                                                联合国的份子钱 p.4</div>
                                        </a></div>
                                </div>
                                <div class="px-3 py-2 border-t border-gray-200">
                                    <div class="flex justify-between">
                                        <div><a href="https://www.youtube.com/playlist?list=PLliocbKHJNwt_NgsZ80l_8z5f6ua-uShq"
                                                target="_blank"><img src="/images/youtube.png" alt="小马技术"
                                                    class="w-5 h-5 opacity-80"></a> <!----></div>
                                        <div class="flex items-center text-xs text-green-700">
                                            11-18 16:33
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="bg-gray-50 p-3 mt-5 h-20 border-gray-800 text-center">
                    <h3>Copyright (C) 小马视频 komavideo.com All rights reserved.</h3>
                    <div><a href="#" class="text-blue-700">Back to top</a></div>
                </div>
            </div>
```

#### 抽取图片信息

请帮我写个Python语言的网页爬虫程序，爬取这个utf-8编码的网页：

```
https://komavideo.com/playlist/economy/index.html
```

我要从这个html代码块中爬取内容，请帮我抽出图片信息，并给我返回完整的url。

Done.

## 小马部落

https://discord.gg/VSKw72P

## 课程文件

+ 小马部落Discord专区共享(四级会员)

## 小马视频频道

https://komavideo.com

## 深学AWS

https://deeplearnaws.com

## 深学Azure

https://deeplearnazure.com/

## 深学GCP

https://deeplearngcp.com/

## Youtube

https://youtube.com/@deeplearncloud


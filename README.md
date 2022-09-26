## JsonTestRunner

执行unittest 用例，输出json结构测试报告供web渲染或保存

输出结构体如下：

```json
{
  "test_list": [
    {
      "style": "Failed",
      "name": "test_json_test_runner1.RunnerTestCase",
      "doc": "",
      "count": 2,
      "Pass": 1,
      "fail": 1,
      "error": 0,
      "cid": "c2",
      "info": [
        {
          "index": "test_json_test_runner1.RunnerTestCase.test_success",
          "name": "test_success",
          "style": "Pass",
          "desc": "",
          "script": "success\n",
          "status": "通过"
        }
      ]
    }
  ],
  "count": 5,
  "Pass": 2,
  "fail": 2,
  "error": 1,
  "passrate": "40.00%",
  "start_time": "2022-09-26 18:09:35",
  "stop_time": "2022-09-26 18:09:36",
  "duration": "0:00:01.003048"
}
```

### 安装

```shell
pip install json-test-runner
```

### 使用

#### 命令行

```shell
jtr -c casepath
```

输出：

```shell
E  test_error (test_json_test_runner.RunnerCase)
F  test_failed (test_json_test_runner.RunnerCase)
ok test_pass (test_json_test_runner.RunnerCase)
F  test_failed (test_json_test_runner1.RunnerTestCase)
ok test_success (test_json_test_runner1.RunnerTestCase)

Time Elapsed: 0:00:01.003048
save report file: /work/json-test-runner/test/report.json
```

#### 引用

```python
from jsontestrunner import Runner

case_path = r'./test'
runner = Runner(case_path).run()  # 执行case
print(runner.stream)  # json结构体
runner.save()  # 保存测试报告为json文件
```
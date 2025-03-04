# 文件名：log_masker.py
"""
    r：只读模式（默认值，不可写入）
"""
import re  # 导入正则表达式模块

def mask_log(input_file,output_file):
    # 定义敏感词正确规则（IP/密码/key）
    patterns = {
        r"\d+\.\d+\.\d+\.\d": "***.***.***.***",  #IP地址
        r"(password|pwd)=\w+": "\\1=***",         #密码字段
        r"[A-Za-z0-9]{32}": "*****************"   #模拟API key脱敏
    }

    # 读取原始日志
    with open(input_file,"r") as f:
        logs = f.readlines()
    
    # 处理每一行日志
    masked_logs = []
    for log in logs:
        for pattern, replacement in patterns.items():
            log = re.sub(pattern, replacement, log)
        masked_logs.append(log)
    
    #保存脱敏后的日志
    with open(output_file,"w") as f:
        f.writelines(masked_logs)
    print(f"日志脱敏完成！已保存{output_file}")

# 示例使用（替换为你的日志路径）
# mask_log("raw.log","maskde.log")
    
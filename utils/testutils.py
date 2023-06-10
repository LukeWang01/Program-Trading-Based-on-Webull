from env_k._secrete import LukeLab_Email
from utils.send_email import send_emails

test_sub = 'test email'
test_msg = 'test from luke to test bcc'
receiver = ['liang11355@gmail.com', 'road_prince@outlook.com', '825860815@qq.com', 'liang11354@icloud.com']

send_emails(LukeLab_Email, receiver, test_sub, test_msg)



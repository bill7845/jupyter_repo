## atom script 사용시 한글 깨짐 문제 해결하기 <br>

1. 코드 삽입 <br>

```
import sys

import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


```

<br><br>

2. 환경변수 설정 <br>

* 제어판 -> 시스템 -> 고급시스템설정 -> 고급탭 -> 환경변수 <br>

![1](https://user-images.githubusercontent.com/35517797/63245028-04a22c80-c29a-11e9-95e2-646a4b2cbcb6.PNG)

<br>

![2](https://user-images.githubusercontent.com/35517797/63245034-079d1d00-c29a-11e9-9b28-6b943c97d165.PNG)

<br>

![3](https://user-images.githubusercontent.com/35517797/63245036-09ff7700-c29a-11e9-8250-ec094c07d0ff.PNG)


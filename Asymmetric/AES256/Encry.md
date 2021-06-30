# AES 256 코드 설명 
## myCipher = myAES(keytext,ivtext)
> myCipher 인스턴스를 생성한다.
> 평문과 IV를 utf-8 방식으로 인코딩해준다.

## ciphered = myCipher.enc(msg)
> myAES 클래스의 enc 함수를 실행
> 우선 평문(plaintext)을 makeEnabled 함수로 보내서 AES 256 의 평문 크기에 맞게 패딩해준다.
> 각 매개변수를 넣은 aes 인스턴스를 생성해준다.
> 인코딩된 평문과 IV 로 [CBC 방식](https://ko.wikipedia.org/wiki/%EB%B8%94%EB%A1%9D_%EC%95%94%ED%98%B8_%EC%9A%B4%EC%9A%A9_%EB%B0%A9%EC%8B%9D)으로 암호화를 시작
## deciphered = myCipher.dec(ciphered)
> 


## portfoilo-site
- 필라테스 관리자 서비스
### poetry
- poetry shell
- poetry install

### 모델 구조
회원(Member)

- 회원ID (PK)
- 이름
- 이메일
- 연락처
- 주소
- 등록일
- 강사(Instructor)

강사ID (PK)

- 이름
- 이메일
- 연락처
- 주소
- 등록일
- 수업(Class)

수업ID (PK)
- 수업명
- 수업 설명
- 수업 시간
- 강사ID (FK: 강사)
- 회원 수업 예약(Reservation)

예약ID (PK)
- 회원ID (FK: 회원)
- 수업ID (FK: 수업)
- 예약 날짜
- 예약 시간
- 예약 상태 (예약 완료, 취소 등)
- 결제(Payment)

결제ID (PK)
- 예약ID (FK: 회원 수업 예약)
- 결제 금액
- 결제 일자
- 결제 수단
- 결제 상태 (결제 완료, 취소 등)

# Algorithm
Boostcamp AI Tech 3기 `#눈#사람` 조의 알고리즘 스터디 저장소입니다.

## ✔ 참여 방법

1. 이 저장소를 git clone 합니다.
2. 자신의 branch를 만듭니다. 
    
    ```bash
    git branch [branch이름]
    ```
    
3. 현재 활성화된 branch를 변경합니다.
    
    ```bash
    git checkout [branch이름]
    ```
    
4. 자신의 `github ID`로 폴더를 생성합니다. (ex. `honggildong`)
5. 생성된 폴더에 자신의 소스코드를 업로드 합니다.
6. git add & git commit을 진행합니다. 이때, `commit 규칙`을 지킵니다.
    
    ```bash
    git add .
    git commit -m "commit 규칙에 맞게 작성"
    ```
    
7. 현재 들어와있는 PR용 branch에 push를 합니다.
    
    ```bash
    git push -u origin [branch이름]
    ```
    
8. 자신이 만든 branch에 들어가서 `Pull Request`를 합니다. (`Compare & pull request` 버튼 클릭)
9. 다른 사람들의 PR을 보고 자유롭게 코드리뷰를 합니다.
10. 해당 문제의 코드리뷰가 끝나면 메인 저장소에 merge 합니다.
    

## ✔ commit 규칙

- **commit 메시지)** `[문제출처] 문제번호 - 문제이름`
- **description (optional))** 문제 url
- **문제 출처 (플랫폼) 작성법)**
    - [BOJ] - 백준
    - [SEA] - 삼성SW Expert Academy
    - [PGS] - 프로그래머스
    - [LTC] - LeetCode
    - 다른 플랫폼의 경우 마음대로 추가해주시면 됩니다.
- 즉, 커밋을 다음과 같이 하면 됩니다.
    
    ```bash
    git commit -m "[BOJ] 1234 - Hello World" -m "https://www.acmicpc.net/problem/1234"
    ```
    

## ✔ Pull Request 규칙

- **PR 제목)** `github ID / [문제출처] 문제번호 - 문제이름`
    
    ```
    honggildong / [BOJ] 1234 - Hello World
    ```
    
- 미리 설정된 Pull Request 양식에 따라 간략하게 작성해주시면 됩니다.
    
    ```markdown
    #### **풀이한 문제**
    - [BOJ] 1234 - Hello World
    ------
    #### **문제 분류**
    - 여기에 작성해주세요
    ------
    #### **대략적인 코드 설명**
    - 여기에 작성해주세요
    ------
    ```

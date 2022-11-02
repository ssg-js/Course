# Javascript 심화

## DOM

- 계층 관계

- DOM 트리의 요소들을 바꿀 수 있는 유일한 언어 -> javascript



## this

- 함수를 선언할 때 this에 객체가 결정되는 것이 아니고, 함수가 어떻게 호출 되었는지에 따라 동적으로 결정됨

- **전역 환경**에서는 **전역 객체(window)** 를 가리킴 (브라우저의 전역 객체는 window)

- 함수 호출시 
  
  - **함수로 호출** 시 : **window**를 가리킴(무조건!!)
  
  - **메서드로 호출** 시 : **. 앞 객체**를 가리킴

- bind를 통해 명시하게 되면 this는 명시한 객체를 가리킨다.
  
  ```javascript
  const obj1 = {
    const innerfunc = funtion () {
        console.log(this)
    }.bind(obj1)
  }
  ```

- **화살표 함수**를 사용시 bind 쓰지 않고 this로 상위 객체를 가리키는 게 가능
  
  -> 화살표 **상위 스코프가 가리키는 this**를 가리킴
  
  ```javascript
  const obj1 = {
      outer : funtion() {
      console.log(this)
      
      const innerFunc = () => {
          console.log(this)
      }
      innerFunc()                // this => obj
    }
  }
  ```

- 콜백함수에서의 this는 각각 다름
  
  - 일반적으로 함수호 호출하므로 this는 window를 가리킴
    
    - setTimeout(func, 5000) : 5초뒤에 func실행
    
            -> 실행의 제어권을 넘김
    
    - forEach
    
            -> 함수이므로 this는 window를 가리킴
  
  - addEventListener의 경우 앞의 객체를 가리킴 -> btn을 가리킴
    
    단, 화살표 함수로 작성할 시 상위 스코프(전역)의 this를 가리키면서 window를 가리킴
    
    ```javascript
    const btn = document.body.querySelector('#btn')
    
    btn.addEventListener('click', funtions (event) {
        console.log(this)
        console.log(this.innerText)
    }
    ```





<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <h1>버튼 박스 제작</h1>
    <div class="box">
      <h2>예약 페이지</h2>
      <h3>시간 선택</h3>
      <s v-for="(time, index) in times" :key="index">
        <button style="cursor:pointer" :style="styleButton" @click="btnEvent">{{ time }}</button>
        <s v-if="index % 5 == 4" ><br></s>
      </s>
    </div>
    
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {
  },
  data: function() {
    return {
      times: [
        "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
        "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
        "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
      ],
      styleButton: {
        backgroundColor: 'white',
        border: 'none',
        width: 'auto',
        color: '#84898C',
        padding: '15px 32px',
        textAlign: 'center',
        textDecoration: 'none',
        display: 'inline-block',
        fontSize: '16px',
      },
    }
  },
  methods: {
    btnEvent: function () {
      console.log('됨')
    }
  },
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap');

#app {
  font-family: 'Noto Sans KR', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #424242;
  margin-top: 60px;
}

.box {
  width: 700px;
  height: auto;
  box-shadow: 1px 2px 10px 1px #828181;
  margin: auto;
  padding: 15px;
}


</style>

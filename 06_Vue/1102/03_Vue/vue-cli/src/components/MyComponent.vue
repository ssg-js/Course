<template>
  <div class="border">
    <h1>싸피 이거는 내가 만든 새로운 컴포넌트다!!!</h1>
    <!-- 3. 등록하기 -->
    <MyComponentItem 
    static-props="Mycomponent에서 보낸 데이터" 
    :dynamic-props="dynamicProps"
    @give-me-ma-money="parentGetEvent"
    @child-input="getDynamicData"
    />
  </div>
</template>

<script>
// 1. 불러오기
import MyComponentItem from '@/components/MyComponentItem'

export default {
  name: 'MyComponent',
  // 2. 등록하기
  components: {
    MyComponentItem,
  },
  // dynamic props
  data: function () {
    return {
      dynamicProps : "It's in data"
    }
  },
  methods: {
    parentGetEvent: function (childData) {
      console.log('용돈 없어!')
      console.log(childData)
      // App.vue 까지 올리기
      this.$emit('toApp', childData) 
    },
    getDynamicData: function(childInputData) {
      console.log(`사용자가 입력한 값은 ${childInputData} 입니다`)
      console.log(childInputData)
    }
  }
}
</script>

<style>
  .border {
    border: solid 1px black;
  }
</style>
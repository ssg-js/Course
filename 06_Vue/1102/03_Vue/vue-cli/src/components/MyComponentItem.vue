<template>
  <div>
    <h3>MyComponent의 하위 컴포넌트</h3>
    <p>{{ staticProps }}</p>
    <p>{{ dynamicProps }}</p>
    <button @click="childToParent">클릭!</button>
    <input @keyup.enter="childInput" type="text" name="" id="" v-model="childInputData">
  </div>
</template>

<script>
export default {
  name: 'MyComponentItem',
  props: {
    staticProps: String,
    dynamicProps: String,
  },
  data: function () {
    return {
      childInputData: null,
    }
  },
  methods: {
    childToParent: function () {
      this.$emit('give-me-ma-money', '나는 자식이 보낸 데이터이다')
    },
    childInput: function () {
      this.$emit('child-input', this.childInputData)
    },
  }
}
</script>

<style>

</style>
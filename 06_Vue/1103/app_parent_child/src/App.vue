<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <h1>App</h1>
    <input type="text" v-model="appData">
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
    <AppParent 
    :app-data="appData" 
    @child-to-app="childToApp"
    @parent-to-app="parentToApp"
    />
  </div>
</template>

<script>
import AppParent from '@/components/AppParent'

export default {
  name: 'App',
  components: {
    AppParent,
  },
  data: function () {
    return {
      appData: '',
      parentData: '',
      childData: '',
    }
  },
  methods: {
    childToApp: function (childData) {
      this.childData = childData
    }, 
    parentToApp: function (parentData) {
      this.parentData = parentData
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

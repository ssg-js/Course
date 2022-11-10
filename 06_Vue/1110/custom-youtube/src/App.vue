<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
  </div>
</template>

<script>
import MainVideo from '@/components/MainVideo'
import SearchBar from '@/components/SearchBar'
import VideoList from '@/components/VideoList'

export default {
  name: 'App',
  components: {
    MainVideo,
    SearchBar,
    VideoList,
  }
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

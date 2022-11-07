// App.vue

<template>
  <div id="app">
    <p>Counter: {{ counter }}</p>
    <p>Counter x2: {{ counterDouble }}</p>
    <p></p>
    <button @click="increaseCounter">increase +</button>
    <button @click="decreaseCounter">decrease -</button>
  </div>
</template>

<script>
export default {
  name: 'App', 
  data: function() {
    return {
    }
  },
  methods: {
    increaseCounter() {
      console.log(this.$store.state.counter)
      this.$store.dispatch('increase')
      // this.counter += 1
    },
    decreaseCounter() {
      this.$store.dispatch('decrease')
      // this.counter -= 1
    },
  },
  computed: {
    counter() {
      return this.$store.state.counter
    },
    counterDouble: function () {
      return this.$store.getters.counterDouble
    },
  },
}
</script>

<style>
</style>

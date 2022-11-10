<template>
  <div>
    <h1>Lunch</h1>
    <button @click="lunchMenu()">Pick Lunch</button>
    <br>
    <p>{{ lunchmenu }}</p>
    <button @click="toLottoButton" v-if="lunchmenu">Lotto 뽑으러</button>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'LunchView',
  data() {
    return {
      lunchmenu: null,
    }
  },
  methods: {
    lunchMenu() {
      this.lunchmenu = _.sample(["국밥", "짜장면", "햄버거", "비빔국수"]);
      console.log(this.lunchmenu)
    },
    toLottoButton() {
      this.$router.push({ name: 'lotto', params: {lunchmenu: this.lunchmenu}})
    }
  },
}
</script>

<style>

</style>
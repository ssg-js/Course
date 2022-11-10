<template>
  <div>
    <h1>{{ lunchmenu }} 먹고 Lotto 추첨</h1>
    <button @click="makeLotto">Pick Numbers</button>
    <p>{{ lottonumbers }}</p>
    <button @click="toLunch">처음으로</button>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'LottoView',
  data () {
    return {
      lottonumbers: null,
      lunchmenu: null,
    }
  },
  methods: {
    makeLotto () {
      const allnum = _.range(1, 46)
      this.lottonumbers = _.sampleSize(allnum, 6)
    },
    toLunch() {
      this.$router.push({ name: 'lunch' })
    },
  },
  created() {
    console.log(this.$route.params)
    this.lunchmenu = this.$route.params.lunchmenu
  }
}
</script>

<style>

</style>
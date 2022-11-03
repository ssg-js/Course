<template>
  <div>
    <h1>AppParent</h1>
    <input type="text" @input="parentToApp($event)">
    <p>appData: {{ appData }}</p>
    <p>childData: {{ childData }}</p>
    <AppChild
    :parent-data="parentData" 
    :app-data="appData"
    @child-to-parent="childToParent"
    />
  </div>
</template>

<script>
import AppChild from '@/components/AppChild'

export default {
  name: 'AppParent',
  components: {
    AppChild,
  },
  props: {
    appData: String,
  },
  data: function () {
    return {
      parentData: '',
      childData: '',
    }
  },
  methods: {
    childToParent: function (childData) {
      this.childData = childData
      this.$emit('child-to-app', childData)
    },
    parentToApp: function (event) {
      this.parentData = event.target.value
      this.$emit('parent-to-app', this.parentData)
    }
  },
}
</script>

<style>

</style>
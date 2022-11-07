<template>
  <div>
    <span @click="updateTodoStatus">{{ todo.title }}</span>
    <button @click="deleteTodo">Delete</button>
  </div>
</template>

<script>
export default {
  name: 'TodoListItem.vue',
  props: {
    todo: Object,
  },
  methods: {
    deleteTodo() {
      // console.log('di')
      this.$store.dispatch('deleteTodo', this.todo)
      // this.$store.commit('DELETE_TODO', this.todo)
    },
    updateTodoStatus() {
      this.$store.dispatch('updateTodoStatus', this.todo)
    },
  }
}
</script>

<style>

</style>
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    counter: 0,
  },
  getters: {
    counterDouble(state) {
      return state.counter * 2
    }
  },
  mutations: {
    CHANGE_COUNTER(state, changedCounter) {
      state.counter = changedCounter
    }
  },
  actions: {
    increase(context) {
      const changedCounter = context.state.counter + 1
      context.commit('CHANGE_COUNTER', changedCounter)
    },
    decrease(context) {
      const changedCounter = context.state.counter - 1
      context.commit('CHANGE_COUNTER', changedCounter)
    }
  },
  modules: {
  }
})

<template>
  <div id="app">
    <b-container class="m-5 p-0">
      <b-row>
        <b-col cols="2">
          logo
          <nav>
            <router-link to="/" @mouseover="menuMouse" :class="textpopup">Home</router-link> 
            <hr>
            <router-link to="/login">Login</router-link> 
            <hr>
            <router-link to="/signup">Signup</router-link> 
            <hr>
            <router-link to="/community">Community</router-link> 
         </nav>
        </b-col>
        <b-col cols="10">
          <router-view/>  
        </b-col>
      </b-row>
    </b-container>
    
  </div>
</template>

<script>
export default {
  data() {
    return {
      textpopup: null,
    }
  },
  methods: {
    menuMouse() {
      this.textpopup = "text-pop-up-top "
    }
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
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

@keyframes text-pop-up-top {
  0% {
    -webkit-transform: translateY(0);
            transform: translateY(0);
    -webkit-transform-origin: 50% 50%;
            transform-origin: 50% 50%;
    text-shadow: none;
  }
  100% {
    -webkit-transform: translateY(-50px);
            transform: translateY(-50px);
    -webkit-transform-origin: 50% 50%;
            transform-origin: 50% 50%;
    text-shadow: 0 1px 0 #cccccc, 0 2px 0 #cccccc, 0 3px 0 #cccccc, 0 4px 0 #cccccc, 0 5px 0 #cccccc, 0 6px 0 #cccccc, 0 7px 0 #cccccc, 0 8px 0 #cccccc, 0 9px 0 #cccccc, 0 50px 30px rgba(0, 0, 0, 0.3);
  }
}

.text-pop-up-top {
	-webkit-animation: text-pop-up-top 0.5s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
	animation: text-pop-up-top 0.5s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
}
</style>

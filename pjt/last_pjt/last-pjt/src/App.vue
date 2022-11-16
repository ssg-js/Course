<template>
  <div id="app">
    <b-container>
      <b-row>
        <b-col cols="1">
          logo
          <nav>
            <router-link to="/">Home</router-link> 
            <hr>
            <router-link to="/login">Login</router-link> 
            <hr>
            <router-link to="/signup">Signup</router-link> 
            <hr>
            <router-link to="/community">Community</router-link> 
         </nav>
        </b-col>
        <b-col cols="11">
          
        </b-col>
      </b-row>
    </b-container>
    
    <router-view/>
  </div>
</template>

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
</style>

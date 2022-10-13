<template>
  <div id="app">
    <!-- <RouterLink to="/helloworld"></RouterLink>
    <RouterLink to="/mylayout"></RouterLink> -->
    <button @click="linkToMyLayout">Category</button>
    <button @click="linkToHelloWorld">Welcome</button>
    <RouterView></RouterView>
  </div>
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  // components: {
  //   HelloWorld
  // }
  methods: {
    linkToMyLayout() {
      this.$router.push('/mylayout')
    },
    linkToHelloWorld() {
      this.$router.push('./helloworld')
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
  margin-top: 60px;
}

;

button {
  color: aqua;
  vertical-align: bottom;
}
</style>

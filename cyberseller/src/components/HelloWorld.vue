<template>
  <LayoutHeader></LayoutHeader>
  <LayoutNavbar></LayoutNavbar>
    <div class="hello">
      <img alt="CyberSeller logo" src="../assets/logo.png">
      <p>
        Your CyberSellers are coming soon!,<br>
        Check the project in detail:
        <a href="https://github.com/saltyfishyjk/CyberSeller" target="_blank" rel="noopener">CyberSeller</a>.
      </p>
    </div>

</template>

<script>
import LayoutHeader from './LayoutComponents/LayoutHeader.vue';
import LayoutNavbar from './LayoutComponents/LayoutNavbar.vue';


export default {
    name: "HelloWorld",
    props: {
        msg: String
    },
    components: { LayoutHeader, LayoutNavbar }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
a {
  color: #42b983;
}
</style>

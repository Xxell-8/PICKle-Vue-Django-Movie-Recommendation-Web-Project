<template>
  <header class="home-header">
    <span class="title orange">PICK</span>
    <span class="title purple">LE</span>
    <!-- <h1>simpLE</h1> -->
    <img class="left-deco" src="../../assets/deco1.svg" alt="">
    <img class="right-deco" src="../../assets/deco2.svg" alt="">
  </header>
</template>

<script>
export default {
  name: 'HomeHeader',
}
</script>

<style scoped>
  .home-header {
    position: relative;
    height: 11rem;
    background-color: white;
    margin-bottom: 2rem;
  }
  .title {
    font-family: 'Roboto', sans-serif;
    font-weight: 900;
    font-style: italic;
    font-size: 7rem;
    color: #F47B0F;
  }
  .orange {
    color: #F47B0F;
  }
  .purple {
    color: #441DB2;
  }
  .left-deco {
    position: absolute;
    top: 0;
    left: 5px;
    width: 12rem;
  }
  .right-deco {
    position: absolute;
    bottom: 10px;
    right: 10px;
    width: 10rem;
  }
</style>
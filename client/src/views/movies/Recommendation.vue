<template>
  <div>
    <h1 class="chapter-title">PICK TODAY's MOVIE</h1>
    <p>오늘의 추천 키워드를 선택해주세요</p>
    <hr>
    <div class="row gap-3 justify-content-center">
      <div class="col-auto my-2" >
        <div class="card h-100">
          <img src="../../assets/recommend/random.svg" alt="random">
        </div>
      </div>
      <div class="col-auto my-2" >
        <div class="card h-100">
          <img src="../../assets/recommend/genre.svg" alt="genre">
        </div>
      </div>
      <div class="col-auto my-2" >
        <div class="card h-100">
          <img src="../../assets/recommend/similar.svg" alt="similar">
        </div>
      </div>
      <div class="col-auto my-2" >
        <div class="card h-100">
          <img src="../../assets/recommend/classic.svg" alt="classic">
        </div>
      </div>
      <div class="col-auto my-2" >
        <div class="card h-100">
          <img src="../../assets/recommend/series.svg" alt="series">
        </div>
      </div>
    </div>

    
  </div>
</template>

<script>

export default {
  components: {
  },
}
</script>

<style scoped>
  .chapter-title {
    font-family: 'Roboto', sans-serif;
    font-weight: 900;
    /* font-style: italic; */
    font-size: 3rem;
    color: #F47B0F;
    -webkit-text-stroke: 0.1rem #fff; 
  }
  hr {
    width: 10rem;
    margin: 1rem auto;
    background-color: #fff;
    border-top: 0.2rem solid #bbb
  }
  .card {
    border: 0;
    border-radius: 0;
    width: 13rem;
    overflow: hidden;
    box-shadow: 15px 15px 25px black;
  }
</style>
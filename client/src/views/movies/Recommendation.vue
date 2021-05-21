<template>
  <div>
    <h1>추천</h1>
    <h2>MovieDetail</h2>
    <!-- Button trigger modal -->
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
      test
    </button>

    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="d-flex align-items-baseline gap-3">
              <h2>기생충</h2>
              <span><i class="fas fa-heartbeat fs-3"></i></span>
              <span><i class="fas fa-star-and-crescent fs-3"></i></span>
              <span><i class="fas fa-eye fs-3"></i></span>
              <span><i class="fas fa-times-circle fs-3"></i></span>
            </div>
            <hr>
            <div>
              <p>2021. 03. 04. 개봉</p>
              <p>전원백수로 살 길 막막하지만 사이는 좋은 기택(송강호) 가족. 장남 기우(최우식)에게 명문대생 친구가 연결시켜 준 고액 과외 자리는 모처럼 싹튼 고정수입의 희망이다. 온 가족의 도움과 기대 속에 박사장(이선균) 집으로 향하는 기우. 글로벌 IT기업 CEO인 박사장의 저택에 도착하자 젊고 아름다운 사모님 연교(조여정)가 기우를 맞이한다. 그러나 이렇게 시작된 두 가족의 만남 뒤로, 걷잡을 수 없는 사건이 기다리고 있었으니…</p>
            </div>
            <hr>
            
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Recommendation',
}
</script>

<style>
  .modal-content {
    border-radius: 0;
    background-color: #1E1F26;
    background-clip: border-box;
    border: 0.2rem solid #F47B0F;
    border-radius: 0;
    border-top: none;
    outline: 0;
  }

  .modal-header {
  border-radius: 0;
  border: none;
  background-color: #F47B0F;
  height: 1rem;
  }

</style>
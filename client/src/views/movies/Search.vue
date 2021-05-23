<template>
  <div class="mt-5">
    <SearchBar/>
    <SearchList/>
  </div>
</template>

<script>
import SearchBar from '@/components/movies/SearchBar'
import SearchList from '@/components/movies/SearchList'

export default {
  name: 'Search',
  components: {
    SearchBar,
    SearchList,
  }
}
</script>

<style scpoed>

</style>
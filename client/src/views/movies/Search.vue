<template>
  <div>
    <h1>Search</h1>
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

<style>

</style>
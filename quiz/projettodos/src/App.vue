<script>

let data = {
  questionnaires: [{id: 0, name: "hello"},{id: 1, name: "questionnaire"}]
}

export default {
  data(){
    return data;
  },
  mounted(){
    fetch('http://localhost:8000/quiz/api/v1.0/questionnaire')
  }
}
</script>

<template>
  <h1>Hello</h1>
  {{ questionnaires[0].name }}
</template>



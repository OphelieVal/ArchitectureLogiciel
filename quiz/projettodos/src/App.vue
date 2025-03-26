<script>

let data = {
  questionnaires: [{id: 0, name: "hello"},{id: 1, name: "questionnaire"}]
}

export default {
  data(){
    return data;
  },
  mounted(){
    fetch('http://localhost:5000/quiz/api/v1.0/questionnaire')
    .then(response => response.json())
    .then(json => {
      this.questionnaires = json
    })
  }
}
</script>

<template>
  <h1>Hello</h1>
  <li v-for="question in questionnaires"> {{ question.name }} </li>
  
</template>



<script>
import SupprQuestionnaire from './components/SupprQuestionnaire.vue';

let data = {
  questionnaires: []
}

export default {
  data(){
    return data;
  },
  methods : {
    get_by_id: function(id) {
        for (let i = 0; i < this.questionnaires.length; i++) {
          if (this.questionnaires[i].id == id) {
            return this.questionnaires[i];
          }
        }
        return null;
      },
    remove_questionnaires($event) {
        this.questionnaires.splice(this.questionnaires.indexOf(this.get_by_id($event.id)), 1)
      },
  },
  mounted(){
    fetch('http://localhost:5000/quiz/api/v1.0/questionnaire')
    .then(response => response.json())
    .then(json => {
      this.questionnaires = json
    })
  },
  components : {SupprQuestionnaire}
}
</script>

<template>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/
dist/css/bootstrap.min.css" integrity="sha384-
rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin
="anonymous">
  <div class="container">
    <h1>Hello</h1>
    <ol>
        <SupprQuestionnaire v-for="item of questionnaires" :questionnaire="item" @remove="remove_questionnaires($event)"></SupprQuestionnaire>
    </ol>
  </div>
  
</template>



<script>

import AjouterQuestionnaire from './components/AjouterQuestionnaire.vue';
import QuestionnaireItem from './components/questionnaireItem.vue';

let data = {
  questionnaires: [{id: 0, name: "hello"},{id: 1, name: "questionnaire"}],
  newQuestionnaire: ''
}

export default {
  data(){
    return data;
  },
  methods: {
    addQuestionnaire() {
      let name = this.newQuestionnaire.trim();
      if (name) {
        this.questionnaires.push({
          name: name,
        });
        this.newQuestionnaire = '';
      }
    }
  },
  mounted(){
    fetch('http://localhost:5000/quiz/api/v1.0/questionnaire')
    .then(response => response.json())
    .then(json => {
      this.questionnaires = json
    })
  },
  components: { QuestionnaireItem, AjouterQuestionnaire }
}
</script>

<template>
  <h1>Hello</h1>
  <li v-for="q of questionnaires" :questionnaire="q">
    <QuestionnaireItem :questionnaire="q">
    </QuestionnaireItem>
    <AjouterQuestionnaire @add="addQuestionnaire"></AjouterQuestionnaire> 
   </li>
</template>



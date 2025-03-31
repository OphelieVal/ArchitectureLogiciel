<script>

import AjouterQuestionnaire from './components/AjouterQuestionnaire.vue';
import QuestionnaireItem from './components/questionnaireItem.vue';

let data = {
  questionnaires: [{id: 0, name: "hello"},{id: 1, name: "questionnaire"}]
}

export default {
  data(){
    return data;
  },
  methods: {
    addQuestionnaire: function () {
      let text = this.newItem.trim();
      if (text) {
        this.todos.push({
          text: text,
          checked: false
        });
        this.newItem = '';
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
  components: { QuestionnaireItem }
}
</script>

<template>
  <h1>Hello</h1>
  <li>
    <QuestionnaireItem
      v-for="q of questionnaires" :questionnaire="q">
    </QuestionnaireItem>
  </li>

</template>



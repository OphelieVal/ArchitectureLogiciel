<script>
import QuestionnaireItem from './components/questionnaire/questionnaireItem.vue';
import AjouterQuestionnaire from './components/questionnaire/AjouterQuestionnaire.vue';
import ModifierQuestionnaire from './components/questionnaire/ModifierQuestionnaire.vue';
import SupprQuestionnaire from './components/questionnaire/SupprQuestionnaire.vue';

import QuestionItem from './components/question/QuestionItem.vue';
import AjouterQuestion from './components/question/AjouterQuestion.vue';

let data = {
  questionnaires: [{id: 0, name: "hello"},{id: 1, name: "questionnaire"}],
  newQuestionnaire: '',
  modifQuestionnaire: null,

  questions: [],
  newQuestion: '',
  questionnaireId: null,
}

export default {
  data(){
    return data;
  },
  methods: {
    addQuestionnaire(name) {
      if (name) {
      const requete = "http://127.0.0.1:5000/quiz/api/v1.0/questionnaire";
      fetch(requete, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name: name }),
      })
      .then(response => {
        if (response.ok) return response.json();
          else throw new Error('Problème ajax: '+response.status);
        }
      )
      .then(data => {
        this.questionnaires.push(data.questionnaire);
      })
      .catch(error => {
        console.error(error);
      });
      }
    },
    updateQuestionnaire(nvQuest) {
      if (nvQuest) {
        const requete = `http://127.0.0.1:5000/quiz/api/v1.0/questionnaire/${nvQuest.id}`;
        fetch(requete, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ name: nvQuest.name }),
        })
        .then(response => {
          if (!response.ok) {
            throw new Error('Problème ajax: ' + response.status);
          }
          return response.json();
        })
        .then(data => {
          const index = this.questionnaires.findIndex(q => q.id === data.id);
          this.questionnaires[index] = data;
          this.modifQuestionnaire = null;
        })
        .catch(error => {
          console.error(error);
        });
      }
    },
    getQuestions(id) {
      if (id) {
      const requete = `http://127.0.0.1:5000/quiz/api/v1.0/questionnaire/${id}/question`;
      fetch(requete, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      })
      .then(response => {
        if (response.ok) return response.json();
          else throw new Error('Problème ajax: '+response.status);
        }
      )
      .then(data => {
        console.log(data)
        this.questions = data
      })
      .catch(error => {
        console.error(error);
      });
      }
    },
    addQuestion(question, idQuestionnaire) {
    if (question && idQuestionnaire) {
      const requete = `http://127.0.0.1:5000/quiz/api/v1.0/questionnaire/${idQuestionnaire}/question`;
      fetch(requete, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ title: question, questionType: "facile", questionnaire_id: idQuestionnaire}),
      })
      .then(response => {
        if (response.ok) return response.json();
        else throw new Error('Problème ajax: ' + response.status);
      })
      .then(data => {
        console.log(data)
        this.questions.push(data.question);
        console.log(this.questions)
      })
      .catch(error => {
        console.error(error);
      });
      }
    },
    get_by_id: function(id) {
        for (let i = 0; i < this.questionnaires.length; i++) {
          if (this.questionnaires[i].id == id) {
            return this.questionnaires[i];
          }
        }
        return null;
      },
    remove_questionnaire($event) {
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
  components: { QuestionnaireItem, AjouterQuestionnaire, ModifierQuestionnaire, SupprQuestionnaire, QuestionItem, AjouterQuestion }
}
</script>

<template>
    <h1>QUIZ</h1>

  <div class="quiz">

  <div class="questionnaires">
  <h2>Questionnaires</h2>
  <li v-for="q of questionnaires" :questionnaire="q">
    <QuestionnaireItem :questionnaire="q"/>
      <SupprQuestionnaire :questionnaire="q" @remove="remove_questionnaire($event)" />
    <button @click="modifQuestionnaire=q">Modifier</button>
    <button @click="getQuestions(q.id), questionnaireId = q.id">voir les questions</button>
    </li>
    <AjouterQuestionnaire @add="addQuestionnaire"/>

    <ModifierQuestionnaire 
      v-if="modifQuestionnaire" :questionnaire="modifQuestionnaire"
      @update="updateQuestionnaire"
    />
  </div>
  <div class="questions">
  <h2>Questions</h2>
    <div v-if="questions">
      <li v-for="quest in questions" :question="quest.idQuestion">
        <QuestionItem :question="quest" />
      </li>
    </div>
    <AjouterQuestion
    v-if="questionnaireId"
    :idQuestionnaire="questionnaireId"
    @add="addQuestion"/>
  </div>
  </div>
</template>

<style>
.quiz {
  display: flex;
  justify-content: space-between;
  gap: 300px;
}
</style>
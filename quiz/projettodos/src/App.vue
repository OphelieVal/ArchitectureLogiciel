<script>
import QuestionnaireItem from './components/questionnaire/questionnaireItem.vue';
import AjouterQuestionnaire from './components/questionnaire/AjouterQuestionnaire.vue';
import ModifierQuestionnaire from './components/questionnaire/ModifierQuestionnaire.vue';
import SupprQuestionnaire from './components/questionnaire/SupprQuestionnaire.vue';

import QuestionItem from './components/question/QuestionItem.vue';
import AjouterQuestion from './components/question/AjouterQuestion.vue';
import SupprQuestion from './components/question/SupprQuestion.vue';
import ModifierQuestion from './components/question/ModifierQuestion.vue';

let data = {
  questionnaires: [{id: 0, name: "hello"},{id: 1, name: "questionnaire"}],
  newQuestionnaire: '',
  modifQuestionnaire: null,

  questions: [],
  newQuestion: '',
  questionnaireId: null,
  modifQuestion: null
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
    get_by_id: function(id) {
      for (let i = 0; i < this.questionnaires.length; i++) {
        if (this.questionnaires[i].id == id) {
          return this.questionnaires[i];
        }
      }
      return null;
    },
    removeQuestionnaire(id) {
      if (id) {
        const requete = `http://127.0.0.1:5000/quiz/api/v1.0/questionnaire/${id}`;
        
        fetch(requete, {
          method: 'DELETE',
          headers: {
            'Content-Type': 'application/json',
          },
        })
        .then(response => {
          if (!response.ok) {
            throw new Error('Problème ajax: ' + response.status);
          }
          return response.json();
        })
        .then(() => {
          this.questionnaires = this.questionnaires.filter(q => q.id !== id);
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
    removeQuestion(idQuestion) {
      const requete = `http://127.0.0.1:5000/quiz/api/v1.0/questionnaire/${this.questionnaireId}/question/${idQuestion}`;
      fetch(requete, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Problème ajax: ' + response.status);
        }
        return response.json();
      })
      .then(() => {
        this.questions = this.questions.filter(q => q.idQuestion !== idQuestion);
      })
      .catch(error => {
        console.error(error);
      });
    },
    updateQuestion(nvQuest) {
      if (nvQuest) {
        const requete = `http://127.0.0.1:5000/quiz/api/v1.0/questionnaire/${this.questionnaireId}/question/${nvQuest.idQuestion}`;
        fetch(requete, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({title: nvQuest.title}),
        })
        .then(response => {
          if (!response.ok) {
            throw new Error('Problème ajax: ' + response.status);
          }
          return response.json();
        })
        .then(data => {
          const index = this.questions.findIndex(q => q.id === data.id);
          this.questions[index].title = nvQuest.title;
          this.modifQuestion = null;
        })
        .catch(error => {
          console.error(error);
        });
      }
    },
  },
  mounted(){
    fetch('http://localhost:5000/quiz/api/v1.0/questionnaire')
    .then(response => response.json())
    .then(json => {
      this.questionnaires = json
    })
  },
  components: { QuestionnaireItem, AjouterQuestionnaire, ModifierQuestionnaire, SupprQuestionnaire, QuestionItem, AjouterQuestion, ModifierQuestion, SupprQuestion}
}
</script>

<template>
    <h1>QUIZ</h1>

  <div class="quiz">

  <div class="questionnaires">
  <h2>Questionnaires</h2>
  <li v-for="q of questionnaires" :questionnaire="q">
    <QuestionnaireItem :questionnaire="q"/>
    <div class="questionnaire-actions">
      <SupprQuestionnaire :questionnaire="q" @remove="removeQuestionnaire(q.id)" />
      <button class="btn btn-dark" @click="modifQuestionnaire=q">Modifier</button>
      <button class="btn btn-info" @click="getQuestions(q.id), questionnaireId = q.id">Voir les questions</button>
    </div>
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
      <li v-for="quest in questions" :question="quest">
        <QuestionItem :question="quest" />
        <SupprQuestion 
          :question="quest" 
          :questionnaireId="questionnaireId" 
          @remove="removeQuestion(quest.idQuestion)"
        />
        <button @click="modifQuestion=quest">Modifier</button>
      </li>
    </div>
    <AjouterQuestion
    v-if="questionnaireId"
    :idQuestionnaire="questionnaireId"
    @add="addQuestion"/>
    <ModifierQuestion
      v-if="modifQuestion" :question="modifQuestion"
      @update="updateQuestion"/>
  </div>
  </div>
</template>

<style>
.quiz {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 80px;
  padding: 30px;
  font-family: Arial, sans-serif;
  min-height: 100vh;
  overflow-y: auto;
}

/* STYLE DES QUESTIONNAIRES */
.questionnaires {
  width: 45%;
  background-color: #f8f9fa;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}

.questionnaires h2 {
  text-align: center;
  color: #333;
  margin-bottom: 20px;
}

.questionnaires li {
  list-style: none;
  background: #ffffff;
  margin: 15px 0;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s;
}

.questionnaires li:hover {
  transform: scale(1.03);
}

/* STYLE DES QUESTIONS */
.questions {
  width: 50%;
  background-color: #eef1f7;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}

.questions h2 {
  text-align: center;
  color: #222;
  margin-bottom: 20px;
}

.questions li {
  list-style: none;
  background: #ffffff;
  margin: 15px 0;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s;
}

.questions li:hover {
  transform: scale(1.03);
}

/* BOUTONS */
button {
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  cursor: pointer;
  margin: 8px; 
  font-size: 16px;
  font-weight: bold;
  transition: background 0.3s ease-in-out, transform 0.1s;
}

button:hover {
  transform: scale(1.05);
}

.btn-autre:hover {
  background-color: #0056b3;
}

.btn-autre:active {
  background-color: #003f7f;
}

button.delete {
  background-color: #dc3545;
}

button.delete:hover {
  background-color: #a71d2a;
}
</style>
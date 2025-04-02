<script>
export default{
    props: {
        questionnaire : Object,
        question : Object
    },
    data() {
        return {
            nvQuestion: this.question
        };
    },
    methods : {
        update: function() {
            this.$emit('update', { idQuestion: this.nvQuestion.idQuestion, title: this.nvQuestion.title, questionnaireId: this.nvQuestion.questionnaire_id });
        }
    },
    emits : ['update'],
};
</script>
<template>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
*    <input id="modifierQuestion" v-model="nvQuestion.title"
        @keyup.enter="update" 
        placeholder="Entrer le nouveau nom"
        type="text"
        class="form-control">
    <button class="btn btn-success" @click="update">Enregistrer</button>
</template>

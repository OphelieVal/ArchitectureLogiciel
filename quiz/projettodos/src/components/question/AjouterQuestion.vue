<script>
export default{
    props: {
        idQuestionnaire : Number,
        questionnaire : Object
    },
    data() {
        return {
            newQuestion: '',
        };
    },
    methods : {
        add: function() {
            let title = this.newQuestion.trim();
            this.$emit('add', title, this.idQuestionnaire); 
            this.newQuestion = '';
        }
    },
    emits : ['add'],
};
</script>
<template>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    <div class="input-group">
        <input v-model="newQuestion" id="ajoutQuestion"
            @keyup.enter="add" 
            placeholder="Ajouter une question"
            type="text"
            class="form-control">
        <span class="input-group-btn">
            <button @click="add"
            class="btn btn-dark"
            type="button">Ajouter</button>
        </span>
    </div>
</template>
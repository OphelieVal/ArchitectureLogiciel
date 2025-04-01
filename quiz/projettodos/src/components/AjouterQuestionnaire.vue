<script>
export default{
    props: {
        questionnaire : Object
    },
    data() {
        return {
            newQuestionnaire: '',
        };
    },
    methods : {
        add: function() {
            let name = this.newQuestionnaire.trim();
            this.$emit('add', name); 
            this.newQuestionnaire = '';
        }
    },
    emits : ['add'],
};
</script>
<template>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    <div class="input-group">
        <input v-model="newQuestionnaire"
            @keyup.enter="add" 
            placeholder="Ajouter un questionnaire à la liste"
            type="text"
            class="form-control">
        <span class="input-group-btn">
            <button @click="add"
            class="btn btn-default"
            type="button">Ajouter</button>
        </span>
    </div>
</template>
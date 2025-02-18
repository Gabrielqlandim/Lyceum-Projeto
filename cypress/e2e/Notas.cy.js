describe('notas', () => {
    let nome = "teste";
    let email = "teste@cesar.school";
    let senha = "123";
    let new_name = "Ronaldinho da Silva";
    let new_class = "2-A";
    let new_date = "2024-05-28";
    let new_date_check = "28 de Maio de 2024";
    let score = "8.50";
    let new_score = "8,50";
    let score2 = "9.60";
    let new_score2 = "9,60";

    before(() => {
        cy.visit('/');
        cy.get('#cadastrar-btn').click();
        cy.get('#nome').type(nome);
        cy.get('#email').type(email);
        cy.get('#senha').type(senha);
        cy.get('#botao').click();
    })

    beforeEach(() => {
        cy.visit('/');
        cy.get('#nome').type(nome);
        cy.get('#senha').type(senha);
        cy.get('#botao').click();
        
        cy.visit('/alunos/');

        cy.get('[name="criar_turma"]').click();
        cy.get(':nth-child(4) > .cadastrar_aluno > .container > form > .form-group > #nome-aluno').type('1-A');
        cy.get('[name="criar_turma_confirmar"]').click();

        cy.get('[name="criar_turma"]').click();
        cy.get(':nth-child(4) > .cadastrar_aluno > .container > form > .form-group > #nome-aluno').type('2-A');
        cy.get('[name="criar_turma_confirmar"]').click();

        cy.get('[name="criar_turma"]').click();
        cy.get(':nth-child(4) > .cadastrar_aluno > .container > form > .form-group > #nome-aluno').type('3-A');
        cy.get('[name="criar_turma_confirmar"]').click();


        cy.get('#cadastrar-botao').click();
        cy.get('#nome-aluno').type('123123123');
        //cy.get('#turma-aluno').select('1-A');
        cy.get('#data-aluno').click();
        cy.get('#data-aluno').type('2024-04-18');
        cy.get('[name="cadastrar_confirmar"]').click();

        cy.get('#cadastrar-botao').click();
        cy.get('#nome-aluno').type('xico ciência');
        //cy.get('#turma-aluno').select('1-A');
        cy.get('#data-aluno').click();
        cy.get('#data-aluno').type('2024-04-26');
        cy.get('[name="cadastrar_confirmar"]').click();

        cy.get('#cadastrar-botao').click();
        cy.get('#nome-aluno').type('tuka maia');
        //cy.get('#turma-aluno').select('3-A');
        cy.get('#data-aluno').click();
        cy.get('#data-aluno').type('2004-08-04');
        cy.get('[name="cadastrar_confirmar"]').click();
    })

    it('colocar nota para um aluno em uma matéria', () => {
        cy.visit('/portugues/');
        cy.get('[action="/notas/"] > .grid-home').click();

        

        cy.get(':nth-child(1) > :nth-child(7) > .cadastrar-botao').click();
        cy.get('#nota-aluno').clear();
        cy.get('#nota-aluno').type(score);
        cy.get('#butao').click();

  
        cy.get('tbody > :nth-child(1) > :nth-child(4)').should('have.text', new_score);
       
    })

    it('colocar nota para mais de um aluno em uma matéria', () => {
        cy.visit('/matematica/');
        cy.get('[action="/notas/"] > .grid-home').click();

        

        cy.get(':nth-child(2) > :nth-child(7) > .cadastrar-botao').click();
        cy.get('#nota-aluno').clear();
        cy.get('#nota-aluno').type(score);
        cy.get('#butao').click();

        cy.get(':nth-child(3) > :nth-child(7) > .cadastrar-botao').click();
        cy.get('#nota-aluno').clear();
        cy.get('#nota-aluno').type(score);
        cy.get('#butao').click();

  
        cy.get('tbody > :nth-child(2) > :nth-child(4)').should('have.text', new_score);
        cy.get('tbody > :nth-child(3) > :nth-child(4)').should('have.text', new_score);
       
    })

    it('colocar nota para mais de um aluno em mais de uma matéria', () => {
        cy.visit('/matematica/');
        cy.get('[action="/notas/"] > .grid-home').click();

        

        cy.get(':nth-child(2) > :nth-child(7) > .cadastrar-botao').click();
        cy.get('#nota-aluno').clear();
        cy.get('#nota-aluno').type(score);
        cy.get('#butao').click();

        cy.get(':nth-child(3) > :nth-child(7) > .cadastrar-botao').click();
        cy.get('#nota-aluno').clear();
        cy.get('#nota-aluno').type(score);
        cy.get('#butao').click();

        cy.visit('/historia/');
        cy.get('[action="/notas/"] > .grid-home').click();

        

        cy.get(':nth-child(1) > :nth-child(7) > .cadastrar-botao').click();
        cy.get('#nota-aluno').clear();
        cy.get('#nota-aluno').type(score2);
        cy.get('#butao').click();

        cy.get(':nth-child(3) > :nth-child(7) > .cadastrar-botao').click();
        cy.get('#nota-aluno').clear();
        cy.get('#nota-aluno').type(score2);
        cy.get('#butao').click();

        cy.visit('/matematica/');
        cy.get('[action="/notas/"] > .grid-home').click();
        cy.get('tbody > :nth-child(2) > :nth-child(4)').should('have.text', new_score);
        cy.get('tbody > :nth-child(3) > :nth-child(4)').should('have.text', new_score);

        cy.visit('/historia/');
        cy.get('[action="/notas/"] > .grid-home').click();
        cy.get('tbody > :nth-child(1) > :nth-child(4)').should('have.text', new_score2);
        cy.get('tbody > :nth-child(3) > :nth-child(4)').should('have.text', new_score2);

       
    })

    it('editar nota para um aluno em uma matéria', () => {
        cy.visit('/portugues/');
        cy.get('[action="/notas/"] > .grid-home').click();

        

        cy.get(':nth-child(1) > :nth-child(7) > .cadastrar-botao').click();
        cy.get('#nota-aluno').clear();
        cy.get('#nota-aluno').type(score);
        cy.get('#butao').click();

        cy.get(':nth-child(1) > :nth-child(7) > .cadastrar-botao').click();
        cy.get('#nota-aluno').clear();
        cy.get('#nota-aluno').type(score2);
        cy.get('#butao').click();

  
        cy.get('tbody > :nth-child(1) > :nth-child(4)').should('have.text', new_score2);
       
    })

    afterEach(() => {
        cy.visit('/editar_alunos/')
        cy.get(':nth-child(1) > :nth-child(10) > .cadastrar-botao').click();
        cy.get(':nth-child(1) > :nth-child(10) > .cadastrar-botao').click();
        cy.get(':nth-child(1) > :nth-child(10) > .cadastrar-botao').click();

        cy.visit('/alunos/');

        cy.get('[name="apagar_turma"]').click();
        cy.get(':nth-child(5) > .cadastrar_aluno > .container > form > .form-group > #turma-aluno').select('1-A');
        cy.get('[name="apagar_turma_confirmar"]').click();

        cy.get('[name="apagar_turma"]').click();
        cy.get(':nth-child(5) > .cadastrar_aluno > .container > form > .form-group > #turma-aluno').select('2-A');
        cy.get('[name="apagar_turma_confirmar"]').click();

        cy.get('[name="apagar_turma"]').click();
        cy.get(':nth-child(5) > .cadastrar_aluno > .container > form > .form-group > #turma-aluno').select('3-A');
        cy.get('[name="apagar_turma_confirmar"]').click();
    })
    
    after(() => {

        cy.visit('/admin/');
        cy.get('#id_username').type("adm");
        cy.get('#id_password').type("123");
        cy.get('.submit-row > input').click(); 
        cy.get('.model-user > th > a').click();
        cy.get('#searchbar').type(nome);
        cy.get('#changelist-search > div > [type="submit"]').click();
        cy.get('.action-select').click();
        cy.get('select').select('Remover usuários selecionados');
        cy.get('.button').click();
        cy.get('div > [type="submit"]').click();
    })

})

describe('faltas', () => {
    let nome = "teste";
    let email = "teste@cesar.school";
    let senha = "123";

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
        cy.get('#cadastrar-botao').click();
        cy.get('#nome-aluno').type('123123123');
        cy.get('#turma-aluno').select('1-A');
        cy.get('#data-aluno').click();
        cy.get('#data-aluno').type('2024-04-18');
        cy.get('[name="cadastrar_confirmar"]').click();

        cy.get('#cadastrar-botao').click();
        cy.get('#nome-aluno').type('xico ciência');
        cy.get('#turma-aluno').select('1-A');
        cy.get('#data-aluno').click();
        cy.get('#data-aluno').type('2024-04-26');
        cy.get('[name="cadastrar_confirmar"]').click();

        cy.get('#cadastrar-botao').click();
        cy.get('#nome-aluno').type('tuka maia');
        cy.get('#turma-aluno').select('3-A');
        cy.get('#data-aluno').click();
        cy.get('#data-aluno').type('2004-08-04');
        cy.get('[name="cadastrar_confirmar"]').click();
    })

    it('marcar falta em um aluno em uma materia', () => {
        cy.visit('/portugues/');
        cy.get('[action="/faltas/"] > .grid-home').click();
        cy.get(':nth-child(1) > :nth-child(5) > .btn').click();
        cy.get('tbody > :nth-child(1) > :nth-child(4)').should('have.text', '1');
    })

    it('retirar falta de um aluno em uma materia', () => {
        cy.visit('/portugues/');
        cy.get('[action="/faltas/"] > .grid-home').click();
        cy.get(':nth-child(1) > :nth-child(6) > .btn').click();
        cy.get('tbody > :nth-child(1) > :nth-child(4)').should('have.text', '0');
    })

    it('marcar falta em multiplos aluno em uma materia', () => {
        cy.visit('/portugues/');
        cy.get('[action="/faltas/"] > .grid-home').click();

        cy.get(':nth-child(1) > :nth-child(5) > .btn').click();
        cy.get(':nth-child(2) > :nth-child(5) > .btn').click();

        cy.get('tbody > :nth-child(1) > :nth-child(4)').should('have.text', '1');
        cy.get('tbody > :nth-child(2) > :nth-child(4)').should('have.text', '1');
    })

    it('retirar falta em multiplos aluno em uma materia', () => {
        cy.visit('/portugues/');
        cy.get('[action="/faltas/"] > .grid-home').click();

        cy.get(':nth-child(1) > :nth-child(6) > .btn').click();
        cy.get(':nth-child(2) > :nth-child(6) > .btn').click();

        cy.get('tbody > :nth-child(1) > :nth-child(4)').should('have.text', '0');
        cy.get('tbody > :nth-child(2) > :nth-child(4)').should('have.text', '0');
    })

    it('marcar falta em multiplos aluno em multiplas materias', () => {
        cy.visit('/portugues/');
        cy.get('[action="/faltas/"] > .grid-home').click();

        cy.get(':nth-child(1) > :nth-child(5) > .btn').click();
        cy.get(':nth-child(1) > :nth-child(5) > .btn').click();
        cy.get(':nth-child(2) > :nth-child(5) > .btn').click();

        cy.get('tbody > :nth-child(1) > :nth-child(4)').should('have.text', '2');
        cy.get('tbody > :nth-child(2) > :nth-child(4)').should('have.text', '1');

        cy.visit('/matematica/');
        cy.get('[action="/faltas/"] > .grid-home').click();

        cy.get(':nth-child(1) > :nth-child(5) > .btn').click();
        cy.get(':nth-child(2) > :nth-child(5) > .btn').click();
        cy.get(':nth-child(2) > :nth-child(5) > .btn').click();

        cy.get('tbody > :nth-child(1) > :nth-child(4)').should('have.text', '1');
        cy.get('tbody > :nth-child(2) > :nth-child(4)').should('have.text', '2');
    })

    it('retirar falta em multiplos aluno em multiplas materias', () => {
        cy.visit('/portugues/');
        cy.get('[action="/faltas/"] > .grid-home').click();

        cy.get(':nth-child(1) > :nth-child(6) > .btn').click();
        cy.get(':nth-child(1) > :nth-child(6) > .btn').click();
        cy.get(':nth-child(2) > :nth-child(6) > .btn').click();

        cy.get('tbody > :nth-child(1) > :nth-child(4)').should('have.text', '0');
        cy.get('tbody > :nth-child(2) > :nth-child(4)').should('have.text', '0');

        cy.visit('/matematica/');
        cy.get('[action="/faltas/"] > .grid-home').click();

        cy.get(':nth-child(1) > :nth-child(6) > .btn').click();
        cy.get(':nth-child(2) > :nth-child(6) > .btn').click();
        cy.get(':nth-child(2) > :nth-child(6) > .btn').click();

        cy.get('tbody > :nth-child(1) > :nth-child(4)').should('have.text', '0');
        cy.get('tbody > :nth-child(2) > :nth-child(4)').should('have.text', '0');
    })

    afterEach(() => {
        cy.visit('/editar_alunos/')
        cy.get(':nth-child(1) > :nth-child(10) > .cadastrar-botao').click();
        cy.get(':nth-child(1) > :nth-child(10) > .cadastrar-botao').click();
        cy.get(':nth-child(1) > :nth-child(10) > .cadastrar-botao').click();
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

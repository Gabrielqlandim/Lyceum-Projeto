describe('historia de filtrar aluno', () => {
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

    it('filtrar alunos por nome em ordem alfabetica com sucesso', () => {
        cy.visit('/alunos/');

        cy.get('tbody > :nth-child(1) > :nth-child(2)').invoke('text').as('name_first');

        cy.get('[onclick="sort(1)"]').click();
        cy.get('[onclick="sort(1)"]').click();

        cy.get('@name_first').then((name_first) => {
            cy.get('tbody > :nth-child(1) > :nth-child(2)').should('have.text', name_first);
        });
    })
    it('filtrar alunos por serie/turma com sucesso', () => {
        cy.visit('/alunos/');

        cy.get('tbody > :nth-child(1) > :nth-child(3)').invoke('text').as('class_first');

        cy.get('[onclick="sort(2)"]').click();
        cy.get('[onclick="sort(2)"]').click();

        cy.get('@class_first').then((class_first) => {
            cy.get('tbody > :nth-child(1) > :nth-child(3)').should('have.text', class_first);
        });
    })
    it('filtrar alunos por data de matricula com sucesso', () => {
        cy.visit('/alunos/');

        cy.get('tbody > :nth-child(1) > :nth-child(4)').invoke('text').as('date_first');
 
        cy.get('[onclick="sort(3)"]').click();
        cy.get('[onclick="sort(3)"]').click();

        cy.get('@date_first').then((date_first) => {
            cy.get('tbody > :nth-child(1) > :nth-child(4)').should('have.text', date_first);
        });
    })       
    it('filtrar alunos por id com sucesso', () => {
        cy.visit('/alunos/');

        cy.get('tbody > :nth-child(1) > :nth-child(1)').invoke('text').as('id_first');
        cy.get('[onclick="sort(0)"]').click(); 
        cy.get('[onclick="sort(0)"]').click();

        cy.get('@id_first').then((id_first) => {
            cy.get('tbody > :nth-child(1) > :nth-child(1)').should('have.text', id_first);
        });
    })
    it('filtrar alunos por varios filtros com sucesso', () => {
        cy.visit('/alunos/');

        cy.get('tbody > :nth-child(1) > :nth-child(1)').invoke('text').as('id_first');

        cy.get('[onclick="sort(1)"]').click();
        cy.get('[onclick="sort(2)"]').click();
        cy.get('[onclick="sort(3)"]').click();
        cy.get('[onclick="sort(0)"]').click();
        
        cy.get('@id_first').then((id_first) => {
            cy.get('tbody > :nth-child(1) > :nth-child(1)').should('have.text', id_first);
        }); 
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
        cy.get(':nth-child(5) > .action-checkbox > .action-select').check();
        cy.get('select').select('Remover usuários selecionados');
        cy.get('.button').click();
        cy.get('div > [type="submit"]').click();
    })
})                  
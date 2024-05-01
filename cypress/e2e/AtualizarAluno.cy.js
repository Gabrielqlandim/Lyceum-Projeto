describe('atualizar aluno', () => {
    let nome = "teste";
    let senha = "123";
    let new_name = "Ronaldinho da Silva";

    it('atualizar aluno', () => {
        cy.visit('/');
        cy.get('#nome').type(nome);
        cy.get('#senha').type(senha);
        cy.get('#botao').click();
        cy.get('#aalunos').click();

        cy.get('tbody > :nth-child(2) > :nth-child(1)').invoke('text').as('id');

        cy.get('[onclick="editar()"]').click();
        cy.get(':nth-child(2) > :nth-child(7) > .cadastrar-botao').click();
        cy.get('#nome-aluno').clear();
        cy.get('#nome-aluno').type(new_name);
        cy.get('#turma-aluno').select('2-A');
        cy.get('#data-aluno').click();
        cy.get('#data-aluno').type('2024-05-28');
        cy.get('.btn').click();

        cy.get('@id').then((id) => {
            cy.get('tbody > :nth-child(2) > :nth-child(1)').should('have.text', id);
            cy.get('tbody > :nth-child(2) > :nth-child(2)').should('have.text', new_name);
            cy.get('tbody > :nth-child(2) > :nth-child(3)').should('have.text', '2-A');
            cy.get('tbody > :nth-child(2) > :nth-child(4)').should('have.text', '28 de Maio de 2024');
        });

        cy.get('[onclick="editar()"]').click();
        cy.get(':nth-child(2) > :nth-child(7) > .cadastrar-botao').click();
        cy.get('#nome-aluno').clear();
        cy.get('#nome-aluno').type('xico ciência');
        cy.get('#turma-aluno').select('1-A');
        cy.get('#data-aluno').click();
        cy.get('#data-aluno').type('2024-04-26');
        cy.get('.btn').click();

    })
})
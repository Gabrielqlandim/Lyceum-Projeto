describe('historia calendario academico', () => {

    let nome = "teste";
    let senha = "123";

    it('add evento', () => {
        cy.visit('/');
        cy.get('#nome').type(nome);
        cy.get('#senha').type(senha);
        cy.get('#botao').click();
        cy.get('#acalendario').click();
        cy.get(':nth-child(18)').click();
        cy.get('#eventTitleInput').type('Novo Evento');
        cy.get('#saveButton').click();
        cy.get('.event').invoke('text').should('have.string', "Novo Evento");
    })
    it('remover evento', () => {
        cy.visit('/');
        cy.get('#nome').type(nome);
        cy.get('#senha').type(senha);
        cy.get('#botao').click();
        cy.get('#acalendario').click();
        cy.get(':nth-child(18)').click();
        cy.get('#eventTitleInput').type('Novo Evento');
        cy.get('#saveButton').click();
        cy.get('.event').click();
        cy.get('#deleteButton').click();
        cy.get(':nth-child(18)').click();
        cy.get('#newEventModal').should('be.visible');
    })
})

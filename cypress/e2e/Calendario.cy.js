describe('historia calendario academico', () => {

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
    })


    it('add evento', () => {
        cy.visit('/home/');

        cy.get('#acalendario').click();
        cy.get(':nth-child(18)').click();
        cy.get('#eventTitleInput').type('Novo Evento');
        cy.get('#saveButton').click();
        cy.get('.event').invoke('text').should('have.string', "Novo Evento");
    })
    it('remover evento', () => {
        cy.visit('/home/');

        cy.get('#acalendario').click();
        cy.get(':nth-child(18)').click();
        cy.get('#eventTitleInput').type('Novo Evento');
        cy.get('#saveButton').click();
        cy.get('.event').click();
        cy.get('#deleteButton').click();
        cy.get(':nth-child(18)').click();
        cy.get('#newEventModal').should('be.visible');
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

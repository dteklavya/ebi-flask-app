from . import db


class Gene_Autocomplete(db.Model):
    
    __tablename__ = 'gene_autocomplete'
    __table_args__ = {'extend_existing': True}
    
    species = db.Column(db.String(255))
    display_label = db.Column(db.String(128))
    stable_id = db.Column(db.String(128))
    location = db.Column(db.String(60))

    def __repr__(self):
        return '<Gene {}>'.format(self.display_label)
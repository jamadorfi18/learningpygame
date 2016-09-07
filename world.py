from vector import Vector
import pygame


BACKGROUND_IMG_FILENAME = 'images/grass.png'

class World:

    def __init__(self):
        self.entities = {'all': pygame.sprite.Group()}
        self.background = pygame.image.load(BACKGROUND_IMG_FILENAME).convert()

    def add_entity(self, entity, kinds=None):
        self.entities['all'].add(entity)
        if not kinds:
            kinds = tuple()
        for kind in kinds:
            if not self.entities.get(kind):
                # First entity of its kind
                self.entities[kind] = pygame.sprite.Group()
            self.entities[kind].add(entity)

    def process(self, time_passed):
        for entity in self.entities['all']:
            entity.process(time_passed)

        return self.detect_collisions()

    def detect_collisions(self):
        # Detect collisions on enemies, if shot, then remove the enemies
        if (self.entities.get('enemies') and
            self.entities.get('ally_shots')):
            for enemy in self.entities['enemies']:
                collisions = pygame.sprite.spritecollide(enemy, self.entities['ally_shots'], True)
                if collisions:
                    self.entities['all'].remove(enemy)
                    self.entities['enemies'].remove(enemy)

        # Detect enemy shots on buildings
        if ('enemy_shots' in self.entities):
            for building in self.entities['buildings']:
                collisions = pygame.sprite.spritecollide(building,
                              self.entities['enemy_shots'], True)
                if collisions:
                    print "Enemy shots detected"
                    pass

        # Detect Sara on buildings
        if ('player' in self.entities):
            for building in self.entities['buildings']:
                collisions = pygame.sprite.spritecollide(building,
                             self.entities['player'], False)
                if collisions:
                    self.entities['player'].collisioned = True
                    self.entities['player'].process_events(events)
                    print self.entities['player'].collisioned
                    pass

        # Detect Sara shots on buildings
        if ('ally_shots' in self.entities):
            for building in self.entities['buildings']:
                collisions = (pygame.sprite.spritecollide(building,
                              self.entities['player'], False) or
                              pygame.sprite.spritecollide(building,
                              self.entities['enemies'], False) or
                              pygame.sprite.spritecollide(building,
                              self.entities['enemy_shots'], True) or
                              pygame.sprite.spritecollide(building,
                              self.entities['ally_shots'], True))
                if collisions:
                    print "DETECTED!!"
                    pass
        return False

    def render(self, surface):
        surface.blit(self.background, (0, 0))
        for entity in self.entities['all']:
            entity.render(surface)

    def get_close_entity(self, name, location, close=100):
        location = Vector(*location)

        for entity in self.entities['all']:
            if entity.name == name:
                distance = location.get_distance_to(entity.location)
                if distance < close:
                    return entity
        return None

    def process_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()

        for entity in self.entities['events']:
            entity.process_events(events)
